#!/usr/bin/env python3
import subprocess
import os
from os import path
from pathlib import Path

def create_dir():
    dir = os.path.join(str(Path.home()), ".data")
    if(path.isdir(dir)):
        pass
    else:
        os.mkdir(dir)
    os.chdir(dir)

def compile_python(code,f_id):
    file = open(f_id+".py", "w")
    file.write(code)
    file.close()
    op1 = subprocess.run(["python3", f_id+".py"],stdout=subprocess.PIPE).stdout.decode('utf-8')
    op2 = subprocess.run(["python3", f_id+".py"],stderr=subprocess.PIPE).stderr.decode('utf-8')
    op2="ER\#003 "+str(op2)
    subprocess.call(["rm",f_id+".py"])
    if(len(op1) != 0):
        return op1
    else:
        return op2
    

def compile_c(code,f_id):
    file = open(f_id+".c", "w")
    file.write(code)
    file.close()
    cm1err = subprocess.run(["gcc", f_id+".c", "-o", f_id+"_c"], stderr = subprocess.PIPE).stderr.decode('utf-8')
    if(len(cm1err) != 0):
        cm1err="ER\#003 "+str(cm1err)
        return cm1err
    else:
        op = subprocess.run(["./"+f_id+"_c"],stdout=subprocess.PIPE).stdout.decode('utf-8')
        subprocess.call(["rm", f_id+".c", f_id+"_c"])
        return op

def compile_cpp(code,f_id):
    file = open(f_id+".cpp", "w")
    file.write(code)
    file.close()
    cm1err = subprocess.run(["g++", f_id+".cpp", "-o", f_id+"_cpp"], stderr = subprocess.PIPE).stderr.decode('utf-8')
    if(len(cm1err) != 0):
        cm1err="ER\#003 "+str(cm1err)
        return cm1err
    else:
        op = subprocess.run(["./"+f_id+"_cpp"],stdout=subprocess.PIPE).stdout.decode('utf-8')
        subprocess.call(["rm", f_id+".cpp", f_id+"_cpp"])
        return op
    
def run(code = "", lang = None, id = 0):
    create_dir()
    f_id = str(id)
    if(code == ""):
        return "ER\#001 Empty code"
    if(lang=='py'):
        return(compile_python(code,f_id))
    elif(lang=='c'):
        return(compile_c(code,f_id))
    elif(lang=='cpp'):
        return(compile_cpp(code,f_id))
    else:
        return "ER\#002 Unsupported language specified."
