a
    E?`  ?                   @   s,   d dl Z d	dd?ZG dd? d?Zedkr(dS )
?    N?   ?   c                 C   s  t | ?}t?|?}t?|?}| d |d< d|d< t| d|? ?D ]D\}}t?| d|d ? ?||d < t?| d|d ? ?||d < q@|d|  }t| |d ? ?D ]d\}}|| }	|| ||	d  d|   ||	< |||	d   }
d| ||	d   ||
 |
  ||	< q?||fS )Nr   ?   r   )?len?numpyZzeros?	enumerateZmean?var)?data?window?	smoothing?size?emar   ?idx?valZparamZjdxZdelta? r   ?C/home/riccio/repositories/ian-tirso/dev/bot/engine/strat0/Engine.py?evaluateEMA   s    

  &r   c                   @   s:   e Zd Zddd?ZdZdd? Zdd? Zd	d
? Zdd? ZdS )?Engine?strat0c                 C   s   d S )Nr   )?self?tagr   r   r   ?__init__    s    zEngine.__init__?
   c                 C   s   dS )Nz!ETH-USD_open,BTC-USD_open,300,10dr   ?r   r   r   r   ?RequestData&   s    zEngine.RequestDatac                 C   s   dS )NzETH,BTCr   r   r   r   r   ?RequestPosition*   s    zEngine.RequestPositionc                 C   s  d}d}d}d}d}d}d}	|d }
|d }|d }||
 }|d	 dkrNd}nd}d
}t |||?\}}|t?|? }|| ||  || k}|| ||  || k }|| ||| |  k}d }|r?|r?|||  }dt|? d }|s?|r?|r?d}|?s
|	?r
|?r
d}|S )Ng      ???2   r   g????????r   FTr   ZBTC?????zBUY-Z000BTCzSELL-ALL-BTC)r   r   Zsqrt?str)r   r	   Zposition?tokenr
   r   ?topZfeeZscaredZgamblerZethZbtc?timeZpairZbuy?ir   r   ZstddevZunderminZovermaxZ
overscared?actionZqtyr   r   r   ?Evaluate0   s:    zEngine.Evaluatec                 C   s   dS )NTr   )r   Zproposalr   r   r   ?Confirmt   s    zEngine.ConfirmN)r   )	?__name__?
__module__?__qualname__r   Zdaysr   r   r$   r%   r   r   r   r   r      s   
Dr   ?__main__)r   r   )r   r   r   r&   r   r   r   r   ?<module>   s   
Z