from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset= Aluno.objects.all()
    serializer_class=AlunoSerializer
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset= Curso.objects.all()
    serializer_class=CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset= Matricula.objects.all()
    serializer_class=MatriculaSerializer

