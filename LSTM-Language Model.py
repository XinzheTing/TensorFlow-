import os
import tarfile
import time
import numpy as np
import tensorflow as tf
import reader   #借助该模块读取数据，并把单词转为唯一的数字编码，以便神经网络处理

class PTBInput(object):
    def __init__(self,config,data,name=None):
        self.batch_size=batch_size=config.batch_size
        self.num_steps=num_steps=config.num_steps
        self.epoch_size=((len(data)//batch_size)-1)//num_steps
        self.input_data,self.targets=reader.ptb_producer(data,batch_size,num_steps,name=name
class PTBModel(object):
    def __init__(self,is_training,config,input_):
        self._input=input_

        batch_size=input_.batch_size
        num_steps=input_.num_steps
        size=config.hidden_size
        vocab_size=config.vocab_size
    #设置默认的LSTM单元
    def lstm_cell():
        return tf.contrib.rnn.BasicLSTMCell(size,forget_bias=0.0,state_is_tuple=True)
    attn_cell=lstm_cell
    if is_training and config.keep_prob<1:
        def attn_cell():
            return tf.contrib.rnn.DropoutWrapper(lstm_cell(),output_keep_prob=config.keep_prob)
    cell=tf.contrib.rnn.MultiRNNCell([attn_cell() for _ in range(config.num_layers)],state_is_tuple=True)
    self._initial_state=cell.zero_state(batch_size,tf.float32)
    
    with tf.device("/cpu:0"):
        embedding=tf.get_variable("embeddiing",[vocab_size,size],dtype=tf.float32)
        input=tf.nn.embedding_lookup(embedding,input_.input_data)
    if is_training and config.keep_prob<1:
        inputs=tf.nn.dropout(inputs,config.keep_prob)

    outputs=[]
    state=self._initial_state
    with tf.variable_scope("RNN"):
        for time_step in range(num_steps):
            if time_step>0:
                tf.get_variable_scope().reuse_variables()
                (cell_output,state)=cell(inputs[:,time_step,:],state)
                outputs.append(cel_output)
    output=tf.reshape(tf.concat(outputs,1),[-1,size])
    softmax_w=tf.get_variable("softmax_w",[size,vocab_size],dtype=tf.float32)
    softmax_b=tf.get_variable("softmax_b",[vocab_size],dtype=tf.float32)
    logits=tf.matmul(output,softmax_w)+softmax_b
    loss=tf.contrib.legacy_sequence_loss_by_example([logits],[tf.reshape(input_.targets,[-1])],[tf.ones([batch_size*num_steps],dtype=tf.float32)])
    self._cost=cost=tf.reduce_sum(loss)/batch_size
    self.final_state=state

    if not is_training:
        return