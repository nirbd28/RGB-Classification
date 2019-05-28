import numpy as np
import Dif
####################
def Parameters_OPT(features, labels, w1, b1, w2, b2, learning_rate, itter_num):
    ########## define
    cost=np.zeros(itter_num)

    ########## itterations
    itter=0
    while 1:
        ##### calculate parameters of foward propagation
        output=Foward_Propagation_All_Features(features, w1, b1, w2, b2)
        ##### calculate cost
        cost[itter]=Calc_Cost(labels, output)

        ##### calculate grad
        w1_grad,b1_grad=Dif.Grad_Layer1(features, labels, w1, b1, w2, b2)
        w2_grad,b2_grad=Dif.Grad_Layer2(features, labels, w1, b1, w2, b2)

        ##### update parameters
        w1-=w1_grad*learning_rate
        b1-=b1_grad*learning_rate
        w2-=w2_grad*learning_rate
        b2-=b2_grad*learning_rate

        itter+=1
        ##### break from loop
        if itter==itter_num:
            break
    return cost,w1,b1,w2,b2

####################
def Calc_Cost(labels, output):
    features_num=np.size(labels)
    cost=0
    for i in range(0,features_num):
        cur_label=labels[i]
        cur_output=output[i]
        cost+=MSE(cur_output, cur_label)
    cost/=features_num
    return cost

####################
def MSE(calc_output, label):
    cost=(calc_output-label)
    cost=np.power(cost,2)
    return cost

####################
def Foward_Propagation(input, w1, b1, w2, b2):
    z=np.matmul(w1,input)+b1
    z_sig=Sigmoid(z)
    y=np.matmul(w2,z_sig)+b2
    y_sig=Sigmoid(y)

    output=y_sig

    return output,z,z_sig,y,y_sig

####################
def Foward_Propagation_All_Features(features, w1, b1, w2, b2):
    n,features_num=np.shape(features)
    output=np.zeros(features_num)
    for i in range(0,features_num):
        input=features[:,i]
        output[i],_,_,_,_=Foward_Propagation(input, w1, b1, w2, b2)
    return output

####################
def Predict(input, w1, b1, w2, b2):
    output,_,_,_,_=Foward_Propagation(input, w1, b1, w2, b2)
    if output>=0.5:
        return 1
    else:
        return 0

####################
def Sigmoid(x):
    y=np.zeros(np.size(x))
    for i in range (0,np.size(x)):
        y[i]=1/(1+ np.exp(-x[i]) )
    return y

####################
def Check_NN(features, labels, w1, b1, w2, b2):
        input_size,features_num=np.shape(features)

        succes_count=0
        for i in range(0,features_num):
            ### cur input/label
            input=features[:,i]
            label=labels[i]
            ### calc output
            recognized_output=Predict(input, w1, b1, w2, b2)
            ### compare
            if(recognized_output==int(label)):
                str='good!!!'
                succes_count+=1
            else:
                str='bad:('
            print('Input:',input,'Label:',label,'Rec Output:',recognized_output,',',str)
        succes_rate=(succes_count/features_num)*100
        print('succes rate:',succes_rate)

####################
def int_to_bin(i,bit):
    if i == 0:
        s= "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    
    for j in range(0,bit-len(s)):
       s='0'+s
    return s
    
####################
def logical_xor(str1, str2):
    str=str1+str2

    if str=='00' or str=='11':
        return '0'
    else:
        return '1'
