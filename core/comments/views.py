from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Comment


@login_required
def comment_delete(request, pk):
    """
    Eliminar un comentario:
    - Solo el autor del post puede borrarlo.
    """
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post

    if request.user != post.author:
        messages.error(request, 'No tienes permiso para eliminar este comentario.')
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comentario eliminado correctamente.')
        return redirect('post_detail', pk=post.pk)

    return render(request, 'comments/comment_confirm_delete.html', {'comment': comment})
