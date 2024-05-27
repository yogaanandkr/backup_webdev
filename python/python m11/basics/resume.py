class sslc:
        sslc_yop = 2016
        sslc_course = 'SSLC'
        def __init__(self, name, sslc_percentage):
            self.name = name
            self.sslc_percentage = sslc_percentage

        def disp_sslc(self):
            print(self.name, self.sslc_course, self.sslc_yop, self.sslc_percentage)

class hse(sslc):
        hse_yop = 2018
        hse_course = 'HSE'
        def __init__(self, name,sslc_percentage, hse_percentage):
            super().__init__(name, sslc_percentage)
            self.hse_percentage = hse_percentage

        def disp_hse(self):
            print(self.name, self.hse_percentage, self.hse_course)

class degree(hse):
        deg_name = 'B.E'
        deg_course = 'ECE'
        deg_yop = 2022
        def __init__(self, name, sslc_percentage, hse_percentage, deg_percentage):
            super().__init__(name, sslc_percentage, hse_percentage)
            self.deg_percentage = deg_percentage

class resume(degree):
        def __init__(self, name, sslc_percentage, hse_percentage, deg_percentage):
            super().__init__(name, sslc_percentage, hse_percentage, deg_percentage)

        def disp_resume(self):
            print(f'''RESUME
    name: {self.name}
    course 1: {self.sslc_course}
    {self.sslc_course} percentage: {self.sslc_percentage}
    course 2: {self.hse_course}
    {self.hse_course} percentage: {self.hse_percentage}
    degree: {self.deg_name}
    {self.deg_name} course : {self.deg_course}
    {self.deg_name} {self.deg_course} percentage: {self.deg_percentage}''')


yoki = resume('Anand', 94, 78, 79.8)
    # yoki.disp_sslc()
yoki.disp_resume()
