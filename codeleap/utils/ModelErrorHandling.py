from rest_framework import serializers

class CustomModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.error_messages['required'] = f'O campo {field_name} é obrigatório.'
            field.error_messages['blank'] = f'O campo {field_name} não pode ficar em branco.'
            field.error_messages['null'] = f'O campo {field_name} não pode ser nulo.'
