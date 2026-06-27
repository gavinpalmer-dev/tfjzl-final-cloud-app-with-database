


Task 2: Register Model Changes
You will now make changes to onlinecourse/admin.py to be able to use the new features you have built.

Open admin.py in IDE

Import new models
At the moment, you are only importing Course, Lesson, Instructor, and Learner in onlinecourse/admin.py

You need to add Question, Choice, and Submission

``` from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission ```
Create QuestionInline and ChoiceInline
Create QuestionInline and ChoiceInline classes so that you could edit them together on one page in the admin site.

Create QuestionAdmin class
Register Question, Choice, and Submission
After you register the new models, you could create a new course with lessons, questions, and question choices using the admin site.

The register decorator: register(*models, site=django.contrib.admin.sites.site)

See the final admin.py here:

python


	from django.contrib import admin
	# <HINT> Import any new Models here
	from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

	# <HINT> Register QuestionInline and ChoiceInline classes here

	class LessonInline(admin.StackedInline):
		model = Lesson
		extra = 5

	class ChoiceInline(admin.StackedInline):
		model = Choice
		extra = 2

	class QuestionInline(admin.StackedInline):
		model = Question
		extra = 2

	# Register your models here.
	class CourseAdmin(admin.ModelAdmin):
		inlines = [LessonInline]
		list_display = ('name', 'pub_date')
		list_filter = ['pub_date']
		search_fields = ['name', 'description']

	class QuestionAdmin(admin.ModelAdmin):
		inlines = [ChoiceInline]
		list_display = ['content']

	class LessonAdmin(admin.ModelAdmin):
		list_display = ['title']

	# <HINT> Register Question and Choice models here

	admin.site.register(Course, CourseAdmin)
	admin.site.register(Lesson, LessonAdmin)
	admin.site.register(Instructor)
	admin.site.register(Learner)
	admin.site.register(Question, QuestionAdmin)
	admin.site.register(Choice)
	admin.site.register(Submission)
Commit your updated code to Github repository.

Assessment
For Option 1: AI-Graded Submission and Evaluation Copy ans Save the public GitHub repository URL of your admin.py file that includes all seven imported classes and the implementations of QuestionInline, ChoiceInline, QuestionAdmin, and LessonAdmin and save it in a text file.

For Option 2: Peer-Graded Submission and Evaluation Take a screenshot of your admin.py file and save it as 02-admin-file.jpeg or 02-admin-file.png.

admin file sample

Create an admin user
Let's create an admin user with the following details:

Username: admin
Email address: leave blank by pressing enter
Password: Your choice, or use p@ssword123
bash

python3 manage.py createsuperuser
Run
Save your changes
Run the Django development server and check if you can add Question and Choice objects using the admin site.

bash

python3 manage.py runserver
Run
Launch Django admin

Assessment
For both Option 1: AI-Graded Submission and Evaluation and Option 2: Peer-Graded Submission and Evaluation Take a screenshot of the Django admin site showing both the “Authentication and Authorization” section and the “OnlineCourse” section, and save it as 03-admin-site.jpeg or 03-admin-site.png.

admin site sample


Creating a Online Course Application

Task 3: Update the Course Detail Template
The content of this lab is licensed under Apache 2.0