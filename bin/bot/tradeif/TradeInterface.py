a
    ???`%  ?                   @   s>   d dl mZ dZdd? ZG dd? d?Zedkr:eed?? d	S )
?    )?LiveCryptoDataz../../trader/offline_walletc                 C   s   t | ??? S ?N)r   Zreturn_data)Zcoins? r   ?I/home/riccio/repositories/ian-tirso/dev/bot/tradeif/cmc/TradeInterface.py?getLiveFrame   s    r   c                   @   s,   e Zd Zdd? Zdd? Zdd? Zdd? Zd	S )
?TradeInterfacec                 C   s   d S r   r   )?self?tagr   r   r   ?__init__
   s    zTradeInterface.__init__c                 C   sf   t td??}|?? }W d   ? n1 s(0    Y  i }|d ?d?d |d< |d ?d?d |d< |S )N?rr   z = ?????ZETH?   ZBTC)?open?WALLET_PATH?	readlines?split)ZrselfZequest?f?xZpositionr   r   r   ?SendPosition   s
    2zTradeInterface.SendPositionc                 C   s2   |? d?}td?}t?d|d v r"d|d v r.d S )N?,zBTC-ETHZBUYr   ZSELLr   )r   r   ?NotImplementedError)r   ?action?data?framer   r   r   ?Propose   s    
zTradeInterface.Proposec                 C   s   t ?dS )NT)r   )r   Zproposalr   r   r   ?Confirm$   s    zTradeInterface.ConfirmN)?__name__?
__module__?__qualname__r
   r   r   r   r   r   r   r   r      s   r   ?__main__zBTC-USDN)ZHistoric_Cryptor   r   r   r   r   ?printr   r   r   r   ?<module>   s
   !