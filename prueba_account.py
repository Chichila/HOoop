"""Programa para chequear que anda Account"""
import atm_machine as atm

cta1=atm.Account(1234,'Silvina',40.0) #Creo una cuenta
cta2=atm.Account(4567,'Silvina',0.0) #Creo otra cuenta

#"Hago un depósito de 20 pesos a la cta1"
cta1.deposit(20)

#"Hago una trasferencia de 40 pesos a la cta2"
cta1.transfer_money(40,cta2)

#"Hago un retiro de la cta1"
cta1.withdraw(20)

#"Hago un chequeo del balance de ambas cuentas"
print('El balance de la cuenta 1 es ', cta1.check_balance()) #40+20-40-20=0
print('El balance de la cuenta 2 es ', cta2.check_balance()) #0+40=40


