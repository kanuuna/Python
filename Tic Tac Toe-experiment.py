#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Creating a game display:


# In[ ]:


def board_maker():
    
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']
    
    return row1, row2, row3


# In[ ]:


board_maker()[0]


# In[ ]:


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']


# In[ ]:


row1


# In[3]:


def game_display():
    print('Here is the board: ')
    print(row1)
    print(row2)
    print(row3)


# In[ ]:


def game_display_new():
    print('Here is the board: ')
    print(row1new)
    print(row2new)
    print(row3new)


# In[4]:


def position_select():
    position = []
    row_select = input('Please select a row (1,2,3)')
    while row_select not in ['1', '2', '3']:
        print('Selection not in range')
        row_select = input('Please select a row (1,2,3)')
    position.append(row_select)
        
    cell_select = input('Please select a cell (1,2,3)')
    while cell_select not in ['1', '2', '3']:
        print('Selection not in range')
        cell_select = input('Please select a cell (1,2,3)')
        
    position.append(cell_select)
    
    return position
  


# In[5]:


def replacement_select():
    replacement = input('Please select which character to input (O/X)')
    
    while replacement not in ['O', 'o', 'X', 'x']:
        print('Please enter a correct input')
        replacement = input('Please select which character to input (O/X)')
    
    return replacement


# In[ ]:


##row1, row2 , row3 , row_select, cell_select


# In[6]:


def replacement_action(row1, row2 , row3, position, replacement):
    
   

    
    if position[0] == '1':
        if position[1] == '1':
            row1[0] = replacement
        if position[1] == '2':
            row1[1] = replacement
        if position[1] == '3':
            row1[2] = replacement
        
    
    if position[0] == '2':
        if position[1] == '1':
            row2[0] = replacement
        if position[1] == '2':
            row2[1] = replacement
        if position[1] == '3':
            row2[2] = replacement
         
        
    if position[0] == '3':
        if position[1] == '1':
            row3[0] = replacement
        if position[1] == '2':
            row3[1] = replacement
        if position[1] == '3':
            row3[2] = replacement    
        
        
    return row1, row2, row3


# In[ ]:





# In[7]:


def cont_selection():
    dec = input('Do you wish to continue or clear? (Y/N/CLR)')
    
    while dec not in ['Y', 'y', 'N', 'n', 'CLR', 'clr']:
        print('Please enter a valid input')
        dec = input('Do you wish to continue or clear? (Y/N/CLR)')
        
    if dec in ['CLR', 'clr']:
        global row1
        global row2
        global row3
        row1 = [' ',' ',' ']
        row2 = [' ',' ',' ']
        row3 = [' ',' ',' ']
        return True
    if dec in ['Y', 'y']:
        return True
    
    if dec in ['N', 'n']:
        print('Thank you for playing! :)')
        return False


# In[10]:


def tic_tac():
    global row1
    global row2
    global row3
    #Initial setup
    game_on = True
    #create board:
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']
    
    print("Welcome to kanuuna's Tic Tac Toe!" )
    game_display()
    
    
    while game_on == True:
      
         #Select position to modify
        positron = position_select()
        #Select which piece to put in
        replacement = replacement_select()
        #Perform replacement
        row1 = replacement_action(row1, row2 , row3, positron, replacement)[0]
        row2 = replacement_action(row1, row2 , row3, positron, replacement)[1]
        row3 = replacement_action(row1, row2 , row3, positron, replacement)[2]
        #Display board again
        game_display()
        #ask to continue
        game_on = cont_selection()
    
    


# In[ ]:


tic_tac()


# In[ ]:




