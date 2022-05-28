# -*- coding: utf-8 -*-

from time import time
import json
import hashlib

# 创建交易
def new_transaction(sender, receive, amount, current_transactions):
    # 向交易列表,追加一条交易信息
    current_transactions.append({
        'sender': sender,
        'receive': receive,
        'amount': amount
    })

# 判断哈希值是否符合前difficulty个值全是0
def valid_proof(hash, difficulty):
    if hash[:difficulty] == '0000':
        return True
    else:
        return False

# 获取当前区块的哈希值
def get_block_hash(block):
    # 把区块的数据转化为json格式(并且按照顺序)
    block_str = json.dumps(block,sort_keys=True)
    # 摘要算法在加密时需要设置编码
    block_str = block_str.encode('UTF-8')
    # 对当前json格式进行加密(顺序是不能改变)
    return hashlib.sha256(block_str).hexdigest()

# 新建一个区块连接到当前的区块链上
def new_block(block_chain, current_transaction):
    block = {
        'index': len(block_chain),
        'timestamp': time(),
        'transaction': current_transaction[:],
        'nounce': -1,
        'pre_hash': None if len(block_chain) == 0 else get_block_hash(block_chain[-1])
    }
    # 挖矿的过程就是通过已知的变量 + Nonce去匹配系统符合条件的hash值的过程
    hash = get_block_hash(block)
    result = valid_proof(hash, 4)
    while(result == False):  # and  or not 是python指定逻辑运算符
        block['nounce'] = block['nounce'] + 1
        hash = get_block_hash(block)
        result = valid_proof(hash, 4)
    # 把区块添加到区块链中
    block_chain.append(block)

# 初始化区块链
block_chain = []
current_transaction = []
# 初始化创世区块
new_block(block_chain, current_transaction)
for i in range(1,5):
    new_transaction("zhangsan","lisi",50,current_transaction)
    new_block(block_chain, current_transaction)
    # 把之前的交易信息清空
    current_transaction = []

for i in range(len(block_chain)):
    print('--->', block_chain[i])

