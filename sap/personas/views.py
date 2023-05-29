from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import PersonaForm
# Create your views here.
from personas.models import Persona


def detalle_persona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, "personas/detalle.html", {"persona": persona})


def nueva_persona(request):
    if request.method == "POST":
        persona_form = PersonaForm(request.POST)
        if persona_form.is_valid():
            # guarda en la base de datos
            persona_form.save()
            return redirect("index")

    else:
        persona_form = PersonaForm()
    # si no es valido y si el metodo es get
    return render(request, "personas/nuevo.html", {"persona_form": persona_form})


def editar_persona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == "POST":
        persona_form = PersonaForm(request.POST, instance=persona)
        if persona_form.is_valid():
            # guarda en la base de datos
            persona_form.save()
            return redirect("index")

    else:
        persona_form = PersonaForm(instance=persona)
    # si no es valido y si el metodo es get
    return render(request, "personas/editar.html", {"persona_form": persona_form})

def eliminar_persona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect("index")