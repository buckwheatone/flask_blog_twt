// Add or remove a like from a post
function like(postId) {
  const likeCount = document.getElementById(`likes-count-${postId}`);
  const likeButton = document.getElementById(`like-button-${postId}`);


  fetch(`/like-post/${postId}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      likeCount.innerHTML = data["likes"];
      if (data["liked"] === true) {
        likeButton.innerHTML = "favorite";
      } else {
        likeButton.innerHTML = "favorite_outline";
      }
    })
    .catch((e) => alert("Could not like post."));
}

// Add functionality to comfirm post deletion 
var postDeleteModal = document.getElementById('postDeleteModal')
var deletePostForm = document.getElementById('deletePostForm') 
postDeleteModal.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  var post_id_to_del = button.getAttribute('data-bs-postid')
  deletePostForm.setAttribute('action', '/delete-post/' + post_id_to_del)

})
