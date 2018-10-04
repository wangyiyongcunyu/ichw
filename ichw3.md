# 高速缓存存储器
## 1.结构 *通用的存储器层次结构为：少量的高速存储器——如CPU中的寄存器，适量的中速存储器——如高速缓冲存储器，大量的低速存储器——如主存。其中，高速缓冲存储器常被置于CPU和主存之间，他在任何时间都含有主存中一部分内容的副本。*
## 2.工作原理 *在存取时，如果内容在高速缓冲存储器中，就立即存取，如果不在，就会被复制在其中，这样，根据*80-20规则，*即计算机通常花费80%的时间读取20%的数据，而高速缓冲存储器可以存储这20%的数据来使存取至少快80%。*