def maior_primo(x):
    a=2
    val=0
    while x>a:
        if x%a==0:
            val=val+1
            a=a+1
        else:
            a=a+1
        if val==0:
            return x
        else:
            return(x-1)