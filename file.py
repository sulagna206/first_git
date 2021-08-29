def active():
    mem_active=[]
    mem_inactive=[]
    with open("Members.txt",'r+') as check_file:
        file=check_file.readlines()
        check_file.truncate(0)
    x=file.pop(0)
    for f in file:
        if('yes' in f):
            mem_active.append(f)
        else:
            mem_inactive.append(f)
    #print(mem_active)
    
    #print(mem_inactive)
    with open ("Members.txt",'a+') as active_mem:
        with open("Inactive.txt",'a+') as inactive_mem:
            active_mem.write(x)
            inactive_mem.write(x)
            for mem1 in mem_active:
                active_mem.write(mem1)
            for mem2 in mem_inactive:
                inactive_mem.write(mem2)

active()