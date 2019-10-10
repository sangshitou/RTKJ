import xadmin
from stu.models import StudentInfo
from xadmin import views


# 然后我们需要创建class，class命名格式最好为类名+Admin
class RtStudentAdmin:
    list_display = ['no', 'name', 'gender', 'age', 'city']
    search_fields = ['no', 'name', 'gender', 'age', 'city', 'school_name']


class GlobalSetting(object):
    site_title = '人通学生管理系统'  # 设置头标题
    site_footer = '人通学生管理系统'  # 设置脚标题
    menu_style = 'accordion'  # 可收缩列


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(StudentInfo, RtStudentAdmin)
