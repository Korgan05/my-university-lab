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
                                                                                            "message": "Student not found"
                                                                                                    }
                                                                                                        
                                                                                                            if status == "active":
                                                                                                                    return {
                                                                                                                                "student_id": student_id,
                                                                                                                                            "access": True,
                                                                                                                                                        "message": "Access granted"
                                                                                                                                                                }
                                                                                                                                                                    
                                                                                                                                                                        return {
                                                                                                                                                                                "student_id": student_id,
                                                                                                                                                                                        "access": False,
                                                                                                                                                                                                "message": "Student status inactive"
                                                                                                                                                                                                    }
                                                                                                                                                                                                    
                                                                                                                                                                                                    # Test examples
                                                                                                                                                                                                    print(check_student_access(1001))
                                                                                                                                                                                                    print(check_student_access(1002))
                                                                                                                                                                                                    print(check_student_access(9999))
                                                                                                                                                                                                    
