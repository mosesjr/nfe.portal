# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api


class Navegacao(ViewletBase):
    def returnSections(self):
        portal = api.portal.get()
        path = '/'.join(portal.getPhysicalPath())
        secoes = portal.portal_catalog(path={'query' : path, 'depth': 1}, portal_type='section', sort_on='id')

        return secoes

    def getSection(self):
        portal = api.portal.get()
        try:
            secao = self.context.secaoID
            folder = portal[secao]
            path = '/'.join(folder.getPhysicalPath())
        except:
            path = '/'.join(portal.getPhysicalPath()) + '/cidadao'
        secoes = portal.portal_catalog(path={'query' : path, 'depth': 1}, portal_type='Folder')

        return secoes

    def getSectionID(self):
        try:
            return self.context.secaoID
        except:
            return 'cidadao'

    def getSegundoNivelTitle(self):
        try:
            titulo = self.context.segundonivel_titulo
            return titulo
        except:
            return False

    def segundoNivel(self, obj):
        try:
            if obj.exibir_menu_de_segundo_nivel:
                if not obj.hasProperty('segundoNivel'):
                    obj.manage_addProperty(id='segundoNivel', type='boolean', value=True)
                if not obj.hasProperty('currentPath'):
                    path = '/'.join(obj.getPhysicalPath())
                    obj.manage_addProperty(id='currentPath', type='string', value=path)
                if not obj.hasProperty('segundonivel_titulo'):
                    titulo = obj.Title()
                    obj.manage_addProperty(id='segundonivel_titulo', type='string', value=titulo)
                else:
                    return True
            else:
                if obj.hasProperty('currentPath'):
                    return True
                else:
                    return False

        except AttributeError:
            if obj.hasProperty('currentPath'):
                return True
            else:
                return False

    def getSegundoNivel(self, obj):
        try:
            path = obj.currentPath
            return obj.portal_catalog(path={'query': path, 'depth': 2})
        except:
            return False

    def checkVisibility(self, obj):
        try:
            if obj.exibir_menu_de_segundo_nivel:
                return False
            else:
                return True
        except AttributeError:
            return True
