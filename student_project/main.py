from fastapi import FastAPI
from database import engine,Base
from api import student_info,score_router,employee1,teacher,class_router


#删除所有表
# Base.metadata.drop_all(bind=engine)
#创建表
# Base.metadata.create_all(bind=engine)
# 创建系统
app = FastAPI(title="学生管理系统",version="2.0")
#导入子路由
app.include_router(student_info.router,tags=["学生管理"])
app.include_router(score_router,tags=["学生成绩"])
app.include_router(employee1.router,tags=["就业模块"])

app.include_router(teacher.router,tags=["老师管理模块"])
app.include_router(class_router,tags=["班级管理"])


#程序启动
@app.get("/")
async def root():
    return {"message": "欢迎来到学生管理系统"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)