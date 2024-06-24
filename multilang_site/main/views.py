from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import activate, gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Article
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Charger le modèle et le tokenizer GPT-2, setup du chatbot
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)


# Vue pour le Chatbot
@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        if user_message:
            inputs = tokenizer.encode(user_message, return_tensors='pt')
            outputs = model.generate(
                inputs,
                max_length=150,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                num_beams=5,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                repetition_penalty=2.0,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
            bot_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            return JsonResponse({'message': bot_response})
        return JsonResponse({'error': 'No message received'})
    return render(request, 'main/chatbot.html')

# Vue de l'article sélectionné
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'main/article_detail.html', {'article': article})

# Permet le changement de langue quand on clique sur le bouton
def switch_language(request, lang_code):
    activate(lang_code)
    return redirect(request.META.get('HTTP_REFERER', '/'))

# Vue pour la page par défaut avec la liste d'articles
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'title': _("List of Articles")
    }
    return render(request, 'main/article_list.html', context)