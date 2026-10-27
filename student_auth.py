def check_student_access(student_id):
            students = {
                            1001: "active",
                            1002: "inactive",
                            1003: "active"
            }

    status = students.get(student_id)

    if status is None:
                    return {
                                        "student_id": student_id,
                                        "access": False,
                                        "message": "\u0421\u0442\u0443\u0434\u0435\u043d\u0442 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d"
                    }

    if status == "active":
                    return {
                                        "student_id": student_id,
                                        "access": True,
                                        "message": "\u0414\u043e\u0441\u0442\u0443\u043f \u0440\u0430\u0437\u0440\u0435\u0448\u0451\u043d"
                    }

    return {
                    "student_id": student_id,
                    "access": False,
                    "message": "\u0421\u0442\u0430\u0442\u0443\u0441 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430 \u043d\u0435\u0430\u043a\u0442\u0438\u0432\u0435\u043d"
    }

# \u041f\u0440\u0438\u043c\u0435\u0440\u044b \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438
print(check_student_access(1001))
print(check_student_access(1002))
print(check_student_access(9999))
