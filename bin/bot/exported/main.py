a
    �*�`�  �                   @   sn  d Z e r.ddlmZ ddlmZ ddlmZ n$ddlmZ ddlmZ ddl	mZ ddl
Z
e
�� Zejdddd	d
� ejddddd� ejddddd� ejddddd� e�� Zejr�dZejr�eej�Zej	r�eej	�Z	ejr�eej�Zedk�rje�� Ze	�e�Ze�� Ze�e�Ze�ee�Zedk�rbedee� � e�e�Z e�!e ��rje�!e � ned� dS )F�    )�Engine)�TradeInterface)�DbInterfaceNz-dz--debugz
debug mode�
store_true)�help�actionz-enz--enginezchoose engineZstrat0)r   �defaultz-dbz--dbifzchoose dbifZcmcz-trz	--tradeifzchoose tradeifT�__main__zaction: zaction: [NO-OPERATION])"�srcZengine.strat0.Enginer   Ztradeif.cmc.TradeInterfacer   Zdbif.tirso.DbInterfacer   ZengineZtradeifZdbif�argparse�ArgumentParser�parser�add_argument�
parse_args�args�debugZ
DEBUG_MODE�__name__ZRequestDataZdatarequestZSendData�dataZRequestPositionZpositionrequestZSendPositionZpositionZEvaluater   �print�strZProposeZproposalZConfirm� r   r   �3/home/riccio/repositories/ian-tirso/dev/bot/main.py�<module>   sT   ����







