#!/usr/bin/env python
# coding: utf-8

# In[12]:


Class_1={
        "name":"AI"
       }
Class_2={
        "name":"CNC"
       }

Students = {
        "student_1001" : 
                    {
                    "name" : "Ali",
                    "class_ai" : Class_1,
                    "marks_ai" : 
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 40,
                            "quiz2" : 45,
                            "mid" : 50,
                            "final" : 55    
                            }
                    },
        "student_1002" :
                    {
                    "name" : "hassan",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
         "student_1003" :
                    {
                    "name" : "saif",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
      "student_1004" :
                    {
                    "name" : "shehroz",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
         "student_1005" :
                    {
                    "name" : "wasif",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
       
         "student_1006" :
                    {
                    "name" : "shahmeer",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
         "student_1007" :
                    {
                    "name" : "usman",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
         "student_1008" :
                    {
                    "name" : "Huzaifa",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
         "student_1009" :
                    {
                    "name" : "Daniyal",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
         "student_1010" :
                    {
                    "name" : "Hamza",
                    "class_ai" : Class_1,
                    "marks_ai" :
                            {
                            "quiz1" : 90,
                            "quiz2" : 95,
                            "mid" : 80,
                            "final" : 85    
                            },
                    "class_cnc" : Class_2,
                    "marks_cnc":
                            {
                            "quiz1" : 41,
                            "quiz2" : 46,
                            "mid" : 51,
                            "final" : 56           
                            }
                    },
       
}


S_Id = input ("Enter Id: ")

S_Id = "student_" + S_Id

STD_Class = input ("Enter Class (AI/CNC):")

STD_Class_1 = "marks_" + STD_Class

STD_Class_2 = "class_" + STD_Class

STD_Exam = input ("Enter Exam Name (quiz1 / quiz2 / mid / final): ")

print ("Marks of" , Students[S_Id]["name"] , "in" , STD_Class, STD_Exam , "exam is" , 
       Students[S_Id][STD_Class_1][STD_Exam])


# In[ ]:




