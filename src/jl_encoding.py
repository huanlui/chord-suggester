class Encoder:
    def __init__(self,all_categories):
        self.category_to_number_dict = {}
        self.number_to_category_dict = {}
        
        for number,category in enumerate(all_categories):
            number_1_based = number + 1
            self.category_to_number_dict[category] = number_1_based
            self.number_to_category_dict[number_1_based] = category
            
        print(f'Category to number dictionary length: {len(self.category_to_number_dict)}')
        print(f'Number to category dictionary length: {len(self.number_to_category_dict)}')

    def to_category(self, number):
        return self.number_to_category_dict[number]
    
    def to_number(self, category):
        return self.category_to_number_dict[category]