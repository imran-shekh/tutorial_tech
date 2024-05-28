from django.db import models

# Create your models here.
# from  datetime import tim

class Signup(models.Model):
    first_name = models.CharField(max_length=100,default="",null=True)
    last_name = models.CharField(max_length=100,default="",null=True)
    email = models.CharField(max_length=100,default="",null=True)
    password = models.CharField(max_length=255,default="",null=True)
    mobile = models.BigIntegerField(null=True)
    gender = models.CharField(max_length=100,default="",null=True)

    def __str__(self):
        return self.first_name
    

class Course_details(models.Model):
    course_name = models.CharField(max_length=100,default="",null=True)
    slug = models.CharField(max_length=100,default="",null=True)
    desc = models.TextField(max_length=200,default="",null=True)
    price = models.IntegerField(default=1,null=True)
    discount =  models.IntegerField(default=1,null=True)
    course_image = models.ImageField(upload_to='static/images/')
    resource = models.FileField(upload_to='resources/course')
    duration  = models.TimeField()

    def __str__(self):
        return self.course_name


class Videos(models.Model):
    video_title= models.CharField(max_length=100,blank=True,null=True)
    video_id = models.CharField(max_length=100,null=True,blank=True)
    video_belong = models.ForeignKey(Course_details,on_delete=models.CASCADE,default=1)
    video_seq = models.IntegerField(null=True, blank=True)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.video_title
    

class Course_info(models.Model):
    desc  = models.CharField(max_length=300, blank=True,null=True)
    course = models.ForeignKey(Course_details,on_delete=models.CASCADE)

    
    class Meta:
        abstract = True


class tag(Course_info):
    pass


class prereq(Course_info):
    pass


class learning(Course_info):
    pass


class User_Course(models.Model):
    user = models.ForeignKey(Signup,on_delete=models.CASCADE)
    course = models.ForeignKey(Course_details,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} - {self.course.course_name}'


class Payment(models.Model):
    order_id = models.CharField(max_length=200,null=True, blank=True)
    payment_id = models.CharField(max_length=200,null=True, blank=True)
    user_info = models.ForeignKey(Signup,on_delete=models.CASCADE)
    course = models.ForeignKey(Course_details,on_delete=models.CASCADE)
    course_info = models.ForeignKey(User_Course,on_delete=models.CASCADE,null=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.order_id


class Ref_Code(models.Model):
    code = models.CharField(max_length=100)
    course = models.ForeignKey(Course_details,on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.code