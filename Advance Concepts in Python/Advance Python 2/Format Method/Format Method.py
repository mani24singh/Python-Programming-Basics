# PROGRAM TO SHOW USE OF FORMAT METHOD IN PYTHON

name = 'Tony stark'
job = 'Industrialist'
type = 'Philanthropist'

# a = f"This is {name}"
# a = "This is {}".format(name)

a = "This is {} and he is a big {}".format(name, job)

b = "we know {1}, the {0} is a {2}".format(name, job, type)

print(a)

print(b)