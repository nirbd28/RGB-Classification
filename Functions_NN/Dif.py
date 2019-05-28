import numpy as np
import Main_Func
####################

def Grad_Layer1(features, labels, w1, b1, w2, b2):
    ##### size
    _,features_num=np.shape(features)
    hidden_layer_n,input_size=np.shape(w1)
    ##### init
    w1_grad=np.zeros((hidden_layer_n,input_size))
    b1_grad=np.zeros((hidden_layer_n,))
    
    for hidden_layer_i in range(0,hidden_layer_n):
        for input_size_i in range(0,input_size + 1 ): #+1 for b
            for features_num_i in range(0,features_num):
                ##### cur parameters
                cur_input=features[:,features_num_i]
                
                _,z,z_sig,y,y_sig=Main_Func.Foward_Propagation(cur_input, w1, b1, w2, b2)
                cur_label=labels[features_num_i]
                cur_z=np.array([z[hidden_layer_i]])
                cur_w2=w2[0,hidden_layer_i]

                ##### mul
                mul1=Dif_Cost(y_sig, cur_label, features_num)
                mul2=Dif_Sigmoid(y)
                mul3=cur_w2
                mul4=Dif_Sigmoid(cur_z)
                all_mul=mul1*mul2*mul3*mul4

                ##### last mul
                if input_size_i!=input_size:
                    last_dif=cur_input[input_size_i]
                    w1_grad[hidden_layer_i,input_size_i]+=all_mul*last_dif
                else: # for b
                    last_dif=1
                    b1_grad[hidden_layer_i]+=all_mul*last_dif
    return w1_grad,b1_grad

####################
def Grad_Layer2(features, labels, w1, b1, w2, b2):
    ##### size
    _,features_num=np.shape(features)
    hidden_layer_n,input_size=np.shape(w1)
    output_size=np.size(b2)
    ##### init
    w2_grad=np.zeros((hidden_layer_n,output_size))
    b2_grad=np.zeros((output_size,))

    for hidden_layer_i in range(0,hidden_layer_n+1):#+1 for b
        for features_num_i in range(0,features_num):
            ##### cur parameters
            cur_input=features[:,features_num_i]
            _,z,z_sig,y,y_sig=Main_Func.Foward_Propagation(cur_input, w1, b1, w2, b2)
            cur_label=labels[features_num_i]

            ##### mul
            mul1=Dif_Cost(y_sig, cur_label, features_num)
            mul2=Dif_Sigmoid(y)
            all_mul=mul1*mul2

            ##### last mul
            if hidden_layer_i!=hidden_layer_n:
                last_dif=z_sig[hidden_layer_i]
                w2_grad[hidden_layer_i]+=all_mul*last_dif
            else: # for b
                last_dif=1
                b2_grad[output_size-1]+=all_mul*last_dif

    w2_grad=np.transpose(w2_grad)
    return w2_grad,b2_grad


####################
def Dif_Cost(input, label, features_num):
    output=2*(1/features_num)*(input-label)
    return output
####################

def Dif_Sigmoid(input):
    output=Main_Func.Sigmoid(input)*(1-Main_Func.Sigmoid(input))
    return output
####################
