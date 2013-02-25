#!/usr/bin/env python
# encoding: utf-8

# 这个文件用于记录课程要求的条件
# 这个文件可以开放给用户编辑，或者是使用代码生成
from preference import *

# 定义时间段，上午，下午，晚上
p1 = [0,1,2,3,4]
p2 = [5,6,7,8,9]
p3 = [10, 11, 12]

# 某门课想要在某时间上
# ID -> (listof preference)
COURSE_PREFERENCE = {
    
}

# 教师想要在某段时间上课的要求可以转化为课程
# 对时间的要求
TEACHER_PREFERENCE = {
    'crh' : prefs(days=[0,1], time=[0,1,2,3,4]),
    'hxy' : prefs(days=[0,1,4], time=p1+p2),
    'dll' : prefs(days=[2,3,4], time=[2,3,4,5,6]),
    'dxs' : prefs(days=[0,1,2,3]),
    'qy'  : prefs(days=[0,1,2]),
    'yxq' : prefs(days=[0,1,2,3]),
    'mew' : prefs(days=[0]),
    'zxj' : prefs(days=[0,1,2,4]),
    'fds' : prefs(days=[0, 2], time=[0,1]),
    'cxn' : prefs_notin(time=p3),
    'hr'  : prefs_special(3, [5,6], 2, p1),

}
