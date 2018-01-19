#!/usr/bin/env python3
'''
  * @time: Created on 17/01/2018 10:36 PM
  * @author: by Ysan

    每一个程序的内存是独立的

    线程 ： 一串指令的集合  存上下文寄存器的组合
    OS 去调用 CPU 的最小单位

    进程 ： 程序并不能单独运行，只有将程序装载到内存中，系统为它分配资源才能运行，而这种执行的程序就称之为进程，  资源的集合
         每一个程序执行的实例

    进程要操作cpu, 必须要先创建一个线程，

    所有在同一个进程里的线程是共享同一块内存空间的

    进程与线程的区别
    线程共享内存空间，进程的内存是独立的
    同一个进程之间线程之间可以直接交流，两个进程想通信，必须通过一个中间代理来实现
    创建新线程很简单，创建新进程需要对其父进程进行一次克隆
    一个线程可以控制和操作同一进程里的其他线程，但是进程只能操作子进程
    对于主线程的修改有可能会影响其他线程，对父进程的修改对子进程没有影响

    python GIL (Global Interpreter Lock)    全局解释器锁
    无论启动多少个线程，有多少个cpu，Python在执行的时候会淡定的在同一时刻只允许一个线程运行
    GIL 并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念

    IO 操作不占用CPU， 计算占用CPU
    python 的多线程  不适合cpu密集操作型的任务， 适合io操作密集型的任务
'''