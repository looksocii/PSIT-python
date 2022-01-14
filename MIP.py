"""M_I_P"""
def main():
    """Docstring"""
    num_a = fun()
    num_b = fun()
    num_c = fun()
    num_d = fun()
    num_e = fun()
    num_f = fun()
    num_g = fun()
    num_h = fun()
    num_i = fun()
    num_j = fun()
    num_k = fun()
    num_l = fun()
    det_y = ((num_a*num_h*num_k)+(num_d*num_g*num_i)+(num_c*num_e*num_l))-\
    ((num_i*num_h*num_c)+(num_l*num_g*num_a)+(num_k*num_e*num_d))
    det_z = ((num_a*num_f*num_l)+(num_b*num_h*num_i)+(num_d*num_e*num_j))-\
    ((num_i*num_f*num_d)+(num_j*num_h*num_a)+(num_l*num_e*num_b))
    print(int((((num_d*num_f*num_k)+(num_b*num_g*num_l)+(num_c*num_h*num_j))-\
    ((num_l*num_f*num_c)+(num_j*num_g*num_d)+(num_k*num_h*num_b)))/(((num_a*\
    num_f*num_k)+(num_b*num_g*num_i)+(num_c*num_e*num_j))-\
    ((num_i*num_f*num_c)+(num_j*num_g*num_a)+(num_k*num_e*num_b)))), int(det_y/\
    (((num_a*num_f*num_k)+(num_b*num_g*num_i)+(num_c*num_e*num_j))-((num_i*num_f*\
    num_c)+(num_j*num_g*num_a)+(num_k*num_e*num_b)))), int(det_z/(((num_a*num_f*\
    num_k)+(num_b*num_g*num_i)+(num_c*num_e*num_j))-((num_i*num_f*num_c)+(num_j*\
    num_g*num_a)+(num_k*num_e*num_b)))))
def fun():
    num = int(input())
    return num
main()
