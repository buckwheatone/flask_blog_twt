function like(postId) {
  const likeCount = document.getElementById(`likes-count-${postId}`);
  const likeButton = document.getElementById(`like-button-${postId}`);
  // const likeIcon = document.getElementsByClassName('like')


  fetch(`/like-post/${postId}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      likeCount.innerHTML = data["likes"];
      if (data["liked"] === true) {
        likeButton.innerHTML = "favorite";
        // likeIcon.innerHTML = 'favorite'

      } else {
        likeButton.innerHTML = "favorite_outline";
        // likeIcon.innerHTML = 'favorite_outline'
      }
    })
    .catch((e) => alert("Could not like post."));
}