'''
GOAL: high level generate image for the screenshot of a state and add to Image table
given: state UUID, config file [img resolution for screenshot, os, browser option]
return: png image of screenshot of a state,
        add a new image object to Image table
'''
from django.core.management.base import BaseCommand, CommandError
from HookCatcher.models import Image, State


def addImgData(stateObj, imgWidth, imgHeight, os, browser):
    imgObj = Image(browserType=browser,
                   operatingSystem=os,
                   width=imgWidth,
                   height=imgHeight,
                   state=stateObj)
    print(imgObj)
    imgObj.save()
    imgObj.delete()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # use state UUID for identification rather thatn commitHash, repo, branch, state names
        parser.add_argument('stateUUID')
        parser.add_argument('imgWidth')
        parser.add_argument('imgHeight')
        parser.add_argument('os')
        parser.add_argument('browser')

    def handle(self, *args, **options):
        try:
            s = State.objects.get(stateUUID=options['stateUUID'])

            try:
                imgWidth = options['imgWidth']
                imgHeight = options['imgHeight']
                os = options['os']
                browser = options['browser']
            except:
                raise CommandError('Please provide all args for command: addScreenshotData <stateUUID> <image width> <image height> <operating system> <browser>')  # noqa: E501

        except State.DoesNotExist:
            raise CommandError('State "%s" does not exist' % options['stateUUID'])
        addImgData(s, imgWidth, imgHeight, os, browser)

        self.stdout.write(self.style.SUCCESS('Added image to database'))