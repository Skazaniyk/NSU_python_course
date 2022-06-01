def f(students):
    return sorted(students,
                reverse=True,
                key=lambda x:len(x['name']) + len(x['surname']
                )
)

students = [
        {
            'name': 'Artem',
            'surname': 'Kravchuck',
            'gpa': 2,
        },
        {
            'name': 'Artem1',
            'surname': 'Kravchuck',
            'gpa': 2.1,
        },
        {
            'name': 'a',
            'surname': 'b',
            'gpa': 5,
        }
    ]
print(f(students))