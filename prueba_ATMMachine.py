"""Programa para chequear que anda ATMMachine"""
import atm_machine as atm

atm1=atm.ATMMachine()

#Genero dos cuentas
atm1.create_new_account(1234,'Silvina',40.0)
atm1.create_new_account(4567,'Silvina',0.0)

#Retiro 20 pesos de la cuenta 1234
atm1.make_a_withdraw(1234,40)

#Deposito 40 pesos en la cuenta 1234
atm1.make_a_deposit(1234,40)

#Tranfiero 40 pesos de la cuenta 1234 a la 4567
atm1.make_a_transfer(1234,4567,40)

#Imprimo el balance de las cuentas
atm1.print_account_balance(1234) #40-40+40-40
atm1.print_account_balance(4567) #0+40
