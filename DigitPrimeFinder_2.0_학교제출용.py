
# 소수 탐색 프로그램
# Developed by bcchickadee, init Feb 28 2020, finalized Jun 20 2020
print('소수 탐색 프로그램')
print('ver 2.0')
print('Developed by bcchickadee, initial release Feb 28 2020, renewed release Jun 20 2020')
print('===========================================\n')

print('프로그램 설명: 이 프로그램은 입력된 숫자열(array) 중에서 발견되는 n자리 소수를 탐색해줍니다.\n')
print('이 프로그램은 2004년 Google사가 낸 광고인 "{first 10-digit prime found in consecutive digits of e}.com" 에서 영감을 얻었습니다.')
print('주의: 매우 큰 수를 입력하면 계산이 오래 걸릴 수 있습니다.')
print('\n===========================================\n')

# 프로그램 설명: 이 프로그램은 입력된 숫자열(array) 중에서 발견되는 n자리 소수를 탐색해줍니다.
# 이 프로그램은 2004년 Google사가 낸 광고인 "{first 10-digit prime found in consecutive digits of e}.com" 에서 영감을 얻었습니다.

import math
# 함수 계산(자릿수 계산)을 위해 math 모듈 필요

CutList=[]
# n자리 수로 잘린 수를 저장해놓을 목록

# 입력된 숫자에서 n자리 array를 추출하여 CutList 목록에 저장하기 위한 NumCutter 함수 정의
def NumCutter(InputNumber, DigitSpace):
    if math.log10(int(InputNumber))+1<int(DigitSpace):
        print('\n\n오류: 탐색 소수의 자릿수는 초기 입력 숫자의 자릿수를 넘을 수 없습니다.')
        #n자리 소수를 array에서 찾으려고 하면, 그 array는 n자리 이상이어야 한다.
    else:
        for Increment in range (0, len(str(InputNumber))-int(DigitSpace)+1):
            CutList.append(int(str(InputNumber)[Increment:Increment+int(DigitSpace)]))
            #n자리씩 잘라서 CutList에 넣음.

PrimesinCutList=[]
# CutList에서 발견되는 각각의 소수를 PrimesinCutList라는 새로운 목록에 저장함.

# 임의의 자연수가 소수인지 판별하기 위한 PrimeDistinguisher 함수 정의
def PrimeDistinguisher(TargetInteger):
    for Dividend in range(2, int(TargetInteger)):
        if round(int(TargetInteger) / float(Dividend))==int(TargetInteger) / float(Dividend):
            break
        #2와 TargetInteger 사이의 약수가 발견되면 프로세스를 중지함.
    else:
        PrimesinCutList.append(TargetInteger)
        #2와 TargetInteger 사이의 약수가 발견되지 않으면 그 수는 소수이므로 PrimesinCutList에 저장함.

# 위에서 정의한 함수들을 묶어주는 PrimeSelectionProcess 함수 정의
# 전반적인 프로그램 진행을 맡음.
def PrimeSelectionProcess(InputNumber, DigitSpace, UserPreferenceforDuplicates):
    if UserPreferenceforDuplicates==str('y') or UserPreferenceforDuplicates==str('Y'):
        NumCutter(InputNumber, DigitSpace)
        for CutNumber in CutList:
            if CutNumber<10**(int(DigitSpace)-1):
                CutList.remove(CutNumber)
            else:
                PrimeDistinguisher(CutNumber)
        for PrimeNumber in PrimesinCutList:
            print(PrimeNumber)
        if len(PrimesinCutList)==0 and math.log10(InputNumber)+1>=DigitSpace:
            print(str(DigitSpace)+'자리의 소수가 발견되지 않았습니다.')
        else:
            print('입니다.')
    elif UserPreferenceforDuplicates==str('n') or UserPreferenceforDuplicates==str('N'):
        NumCutter(InputNumber, DigitSpace)
        for CutNumber in CutList:
            if CutNumber<10**(int(DigitSpace)-1):
                CutList.remove(CutNumber)
            else:
                PrimeDistinguisher(CutNumber)
        for PrimeNumber in set(PrimesinCutList):
            print(PrimeNumber)
        if len(PrimesinCutList)==0 and math.log10(InputNumber)+1>=DigitSpace:
            print(str(DigitSpace)+'자리의 소수가 발견되지 않았습니다.')
        else:
            print('입니다.')
    elif UserPreferenceforDuplicates!=str('y') and UserPreferenceforDuplicates!=str('Y') and UserPreferenceforDuplicates!=str('n') and UserPreferenceforDuplicates!=str('N'):
        print('오류: 올바른 중복 표시 옵션을 선택하십시오.\n')


while True:
    InputNumber=input('소수를 찾고자 하는 숫자열을 입력하십시오.\n숫자열(array): ')
    DigitSpace=input('\n찾고자 하는 소수의 자릿수를 입력하십시오.\n자릿수: ')
    UserPreferenceforDuplicates=input('\n중복된 소수를 모두 표현하시겠습니까? (y/n)\n선택: ')
    print('\n'+InputNumber+'에서 발견된 '+DigitSpace+'자리 소수는:\n')
    PrimeSelectionProcess(InputNumber, DigitSpace, UserPreferenceforDuplicates)
    PrimesinCutList.clear()
    CutList.clear()
    ContinuationKeyInput=input('\n계속하려면 Enter를 누르십시오...\n')
    del ContinuationKeyInput
    print('\n===========================================\n\n')
