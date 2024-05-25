from calc import Calcnums
panic = 'Выдача паники, так как'

"""Переводит римские в арабские + проверка на цифры"""
def rimsk_to_arab(lst_nums, list_of_actions):#, str_act):# На входе если int (n1,n2,) str(str_act), то они же, если римские n1,n2 то переводим их в арабские
    #если разные, то 'smth' 'smth'
    action_lst = ['+', '-', '*', '/']
    nums_rimsk = ['I','II','III','IV','V', 'VI','VII','VIII','IX','X']
    nums_arabsk =[str(i) for i in range(0,10)]
    dic_nums ={1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V', 6 : 'VI', 7 : 'VII', 8 : 'VIII', 9 : 'IX', 10:  'X'}
    new_lst_rimsk=[]
    new_lst_arabsk=[]
    for j in lst_nums:# create 2 lists arabsk and rimsk 
        if j in nums_rimsk:
            for k,v in dic_nums.items():
                if v == j:
                    new_lst_rimsk.append(k)
        elif j in nums_arabsk:
            new_lst_arabsk.append(j)
    new_lst = new_lst_rimsk+new_lst_arabsk
    if list_of_actions[0] not in action_lst:
        list_of_actions='smth'
    if len(new_lst_arabsk) == 1 and len(new_lst_rimsk) == 1 or len(new_lst_arabsk) == 0 and len(new_lst_rimsk) == 1\
        or len(new_lst_arabsk) == 1 and len(new_lst_rimsk) == 0 or len(new_lst_arabsk) == 0 and len(new_lst_rimsk) == 0:# Варианты неправильных цифр
        return 'smth', list_of_actions
    elif len(new_lst_arabsk) == 2 or len(new_lst_rimsk) == 2:
        return new_lst, list_of_actions
    

"""Найдем действие"""
def find_action(list_in):
        action_lst = ['+', '-', '*', '/']
        list_of_actions=[]
        for i in list_in:
            if i in action_lst:
                list_of_actions.append(i)
        if len(list_of_actions) !=1:# Пробежались по действиям ,если ни одного или больше 1, то 
            print(f'{panic} Действие должно быть одно')
            return('smth', 'smth')
        elif len(list_of_actions) == 1:
            list_out = list_in.split(f"{list_of_actions[0]}")
            return list_of_actions, list_out

if __name__ == '__main__':
    
    print('Input')
    s =  input()
    list_of_actions, lst_nums = find_action(s) # Получили список с дейсвием и список с запятой, вместо действиия между 
    #числами в случае если есть действие и если нет действия. то 'smth'=list_of_actions 'smth' - это значит, что ошибка
    lst_nums, list_of_actions, = rimsk_to_arab(lst_nums, list_of_actions)
    if list_of_actions!='smth' and lst_nums!='smth':
        num1 = lst_nums[0]
        num2 = lst_nums[1]
        action = list_of_actions[0]
        result = Calcnums(num1, num2, action)
        print("Output")
        print(result.result_nums())
   
    elif list_of_actions =='smth' and lst_nums=='smth':
        print(f'{panic}. Должно быть одно действие и Invalid figures were in input')
    elif list_of_actions =='smth':
        print('Output')
        print(f'{panic}. Должно быть одно действие')
    elif lst_nums == 'smth':
        print(f'{panic} Invalid figures were in input')
            
    
        