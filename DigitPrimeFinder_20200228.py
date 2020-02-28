# Prime Finder Program
# 소수 탐색 프로그램
# Developed by bcchickadee, Feb 28 2020
print('Prime Finder Program')
print('소수 탐색 프로그램')
print('ver 1.5')
print('Developed by bcchickadee, Feb 28 2020')
print('===========================================\n')

print('Program Description: This program finds n-digit prime numbers found in the digits of a given array of numbers.')
print('프로그램 설명: 이 프로그램은 입력된 문자(숫자)열 중에서 발견되는 n자리 소수를 탐색해줍니다.\n')
print('This program is inspired by the 2004 Google billboard advert: {first 10-digit prime found in consecutive digits of e}.com.')
print('이 프로그램은 2004년 Google사가 낸 광고인 "{first 10-digit prime found in consecutive digits of e}.com" 에서 영감을 얻었습니다.')
print('\nWarning: Please refrain from calculating extremely big numbers, as it takes a substantial amound of time.')
print('주의: 매우 큰 수를 입력하면 계산이 오래 걸릴 수 있습니다.')
print('===========================================\n')

# Program Description: This program finds n-digit prime numbers found in the digits of a given array of numbers.
# 프로그램 설명: 이 프로그램은 입력된 문자(숫자)열 중에서 발견되는 n자리 소수를 탐색해줍니다.
# This program is inspired by the 2004 Google billboard advert: {first 10-digit prime found in consecutive digits of e}.com.
# 이 프로그램은 2004년 Google사가 낸 광고인 "{first 10-digit prime found in consecutive digits of e}.com" 에서 영감을 얻었습니다.

import math
# math module required for function calculation.
# 함수 계산을 위해 math 모듈 필요

CutList=[]
# List for numbers "cut up" to n-digit numbers, processed by the function below
# n자리 수로 잘린 수를 저장해놓을 목록

# NumCutter function definition for "cutting up" the input number into n-digit numbers and putting them to the CutList group
# 입력된 숫자에서 n자리 자연수를 추출하여 CutList 목록에 저장하기 위한 NumCutter 함수 정의
def NumCutter(InputNumber, DigitSpace):
    if math.log10(InputNumber)+1<DigitSpace:
        print('\n\nError: The number of digits of the prime number cannot exceed the number of the initial input number.')
        print('오류: 탐색 소수의 자릿수는 초기 입력 숫자의 자릿수를 넘을 수 없습니다.')
    else:
        for Increment in range (0, math.floor(math.log10(InputNumber))-DigitSpace+2):
            CutNumber=math.floor(InputNumber/(10**Increment))-(10**DigitSpace)*math.floor(InputNumber/(10**(Increment+DigitSpace)))
            CutList.append(CutNumber)

# PrimeDistinguisher function definition for deciding whether an integer is a prime number
# 임의의 자연수가 소수인지 판별하기 위한 PrimeDistinguisher 함수 정의

DivisorList=[]
# List of Divisors, automatically added to the list by the function below
# 함수로부터 산출되는 약수들을 자동으로 담을 목록

def PrimeDistinguisher(TargetInteger):
    for Dividend in range(1, int(TargetInteger)+1):
        if round(int(TargetInteger) / float(Dividend))==int(TargetInteger) / float(Dividend):
            DivisorList.append(Dividend)
    if len(set(DivisorList))==2:
        # If the number of divisors is 2, then that number is a prime number.
        # 약수의 개수가 2이면, 그 수는 소수임.
        DivisorList.clear()
        return True
    else:
        # If the number of divisors is not 2, then that number is not a prime number.
        DivisorList.clear()
        return False


# For every element in CutList, we tell if each number is a prime number.
# CutList의 각각의 원소에 대하여 그 수가 소수인지를 판별합니다.

PrimesinCutList=[]
# For every prime number detected in the CutList, we send them to a new list called PrimesinCutList.
# CutList에서 발견되는 각각의 소수를 PrimesinCutList라는 새로운 목록에 저장합니다.

def PrimeSelectionProcess(InputNumber, DigitSpace):
    NumCutter(InputNumber, DigitSpace)
    for CutNumber in CutList:
        if PrimeDistinguisher(CutNumber)==True:
            PrimesinCutList.append(CutNumber)
            print(CutNumber)
    if len(PrimesinCutList)==0:
        print('No '+str(DigitSpace)+'-digit primes numbers have been found.\n'+str(DigitSpace)+'자리의 소수가 발견되지 않았습니다.')

# PrimeSelectionProcess function definition for screening primes out of the CutList.
# CutList에서 소수를 골라내기 위한 PrimeSelectionProcess 함수 정의

while True:
    InputNumber=input('Enter the array of number in which you would like to find prime numbers.\n소수를 찾고자 하는 숫자열을 입력하십시오.\nArray / 숫자열: ')
    DigitSpace=input('\nEnter the number of digits the prime number should have.\n찾고자 하는 소수의 자릿수를 입력하십시오.\nNumber of digits / 자릿수: ')
    print('\nThe list of '+DigitSpace+'-digit prime numbers found in '+InputNumber+' is:\n'+InputNumber+'에서 발견된 '+DigitSpace+'자리 소수는:\n')
    PrimeSelectionProcess(int(InputNumber), int(DigitSpace))
    print('\n===========================================\n\n')
    PrimesinCutList.clear()
    CutList.clear()
