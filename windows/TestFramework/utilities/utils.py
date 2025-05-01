class Utils :

    def assertListItmesTxt(self,value_list,value):
        for value in value_list:
            assert value.text == value 