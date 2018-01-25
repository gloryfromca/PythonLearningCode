class GetInfoFromCalldetail(object):
    """
    the class consists of call_detail_str json_obejct from which some inner objects are created. 
    """
    
    def __init__(self, call_detail_str):
        """
        form dictStructure by nested objects.
        items of different levels shouldn't have same name.
        items have buffers for not get repeatedly. 
        """
    
        # top_level should be in the front of structureList
        structureList = [
         ("user_mobile",str,None),
         ("real_name",str,None),
         ("channel_attr",str,None),
         ("channel_src",str,None),
         ("task_data",dict,None),
         ("bill_info",list, "task_data"),
         ("account_info",list, "task_data"),
         ("payment_info",list, "task_data"),
         ("call_info",list, "task_data")
        ]
        
        # i[2] is str; attrs[i[2]] is class
        def inner_get(self, defaultValue = StatusField.getNothingDefaultValue):
            try:
                if self.context is not None:
                    return self.context
                return self.holder.get(self)
            except Exception as e:
                return Result(defaultValue, StatusField.failed)
                print(e)
                
        for name_str, type_class, pLevel_str in structureList:
            setattr(self, name_str, type(
                name_str,
                (object,),
                {
                "name":name_str,
                "type":type_class,
                "pLevel":None if pLevel_str is None else getattr(self, pLevel_str),
                "context":None,
                "get":inner_get,
                "holder":self,  
                })()
                )
            
        self.call_detail_dict = json.loads(call_detail_str)
        self.getNothingDefaultValue = StatusField.getNothingDefaultValue
        self.MainNode = None
        self.OtherNodesAndRelations = None
    
    def get(self, innerClassInstance=None):
        result = self.call_detail_dict
        
        if innerClassInstance is None:
            return result
        if innerClassInstance.context is not None:
            print("命中")
            return innerClassInstance.context
        
        get_list = [innerClassInstance.name, ]
        classIterator = innerClassInstance
        while(classIterator.pLevel is not None):
            classIterator = innerClassInstance.pLevel
            get_list.insert(0, classIterator.name)
        for name in get_list:
            try:
                result = result.get(name, self.getNothingDefaultValue)
            except Exception as e:
                finalResult = Result(result, StatusField.failed, (get_list, e))
                innerClassInstance.context = finalResult
                return finalResult
        finalResult = Result(result, StatusField.succeed)
        innerClassInstance.context = finalResult
        return finalResult
        
    def getMainNode(self):
        # InfoBuffer
        if self.MainNode is not None:
            print("命中")
            return self.MainNode
        result = {}
        try: 
            get_list = [
                self.user_mobile, self.real_name, self.channel_attr, self.channel_src,
                       ]
            for getItem in get_list:
                    getResult = self.get(getItem)
                    item_result = getResult.result 
                    item_status = getResult.status
                    result[getItem.name] = item_result 

            get_parser_list = [
                self.payment_info, self.bill_info, self.account_info, self.call_info,
            ]
            parser_list = [
                InfoParser.PaymentInfoParser, 
                InfoParser.BillInfoParser, 
                InfoParser.AccountInfoParser,
                InfoParser.CallInfoParser,
                
            ]
            for getParseItem, parserItem  in zip(get_parser_list, parser_list):
                getResult = parserItem(self.get(getParseItem)) 
                item_result = getResult.result 
                item_status = getResult.status
                result[getParseItem.name] = item_result 
                
        except Exception as e:
            raise e
            
        finally:
            self.MainNode = result
        
        return result

    def getOtherNodesAndRelations(self):
        # InfoBuffer
        if self.OtherNodesAndRelations is not None:
            print("命中")
            return self.OtherNodesAndRelations
        try: 
            get_parsed = self.call_info
            parser = InfoParser.OtherNodesAndRelationshipsFromCallInfoParser
            getResult = parser(self.get(get_parsed))
            result = getResult.result 
            status = getResult.status                
        except Exception as e:
            raise e
        finally:
            self.OtherNodesAndRelations = result
        
        return result
    
    def getOtherNodes(self):
        pass
    
    def getRelations(self):
        pass    
