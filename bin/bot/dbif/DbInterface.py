a
    ?@?`?  ?                   @   s.   d dl mZ dd? ZG dd? d?Zedkr*dS )?    )?HistoricalDatac                 C   s   t | ||??? S ?N)r   Zretrieve_data)Zcoin?grain?date? r   ?C/home/riccio/repositories/ian-tirso/dev/bot/dbif/cmc/DbInterface.py?getFrame   s    r   c                   @   s   e Zd Zdd? Zdd? ZdS )?DbInterfacec                 C   s   d S r   r   )?self?tagr   r   r   ?__init__
   s    zDbInterface.__init__c                 C   s?   |? d?}t|d ?}t|d ?d??}d| | }|d ?d?}|d ?d?}t||d	?}|d
 j}	|jj}
t||d	?}|d
 j}|jj}t|
?D ]}|
|?||?kr? d S q?t|?}|	d| d? |d| d? |
d| d? fS )N?,???????????di?Q r   Z_open?   z2021-04-23-00-00?open)?split?int?stripr   ?values?index?	enumerate)r
   Zrequest?rawr   ZdaysZticksZcoin1Zcoin2Z	dataFrameZx1?t1Zx2?t2?ir   r   r   ?SendData   s"    


zDbInterface.SendDataN)?__name__?
__module__?__qualname__r   r   r   r   r   r   r	      s   r	   ?__main__N)ZHistoric_Cryptor   r   r	   r   r   r   r   r   ?<module>   s   <