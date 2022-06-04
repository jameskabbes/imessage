from setuptools import setup

if __name__ == '__main__':
    setup(
    package_data={'kabbes_imessage': 
        [ 
            'message_mediums/iMessage.applescript',
            'message_mediums/SMS.applescript'
        ]
        }
    )