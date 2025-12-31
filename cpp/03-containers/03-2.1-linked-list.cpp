


// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list
// DO NOT USE -> instead, use std::list

#include <functional>
#include <stdint.h>

struct my_linked_list {
  struct link {
    link* next_link = nullptr;
    void* user_data = nullptr;
  };

  link* head_link = nullptr;
  uint32_t size = 0;

  static void reset_link(link& old_link) {
    old_link.next_link = nullptr;
    old_link.user_data = nullptr;
  }

  void add_link_to_list(link& new_link) {
    // add as head of list
    // -> this is FAST

    // FROM: (headLink) -> ???
    // TO:   (headLink) -> (newLink) <--> ???

    new_link.next_link = this->head_link;
    this->head_link = &new_link;

    this->size += 1;
  }

  void remove_link_from_list(my_linked_list& list, link& old_link) {
    // remove from list
    // -> this is SLOW
    // ---> need to find the link inside the list first
    // ---> need to find the link inside the list first

    if (is_empty_list(list))
      return;

    if (list.head_link == &old_link) {
      // if removing the head -> replace it with the head's next link
      list.head_link = list.head_link->next_link;
    }
    else {

      // find link to remove

      link* curr_link = list.head_link;
      while (curr_link) {
        // found the link to remove?
        if (curr_link->next_link == &old_link) {
          // yes -> replace previous link next's value with this link's next link
          curr_link->next_link = old_link.next_link;
          break;
        }
        // callback(static_cast<T*>(curr_link->user_data));
        curr_link = curr_link->next_link;
      }

    }

    reset_link(old_link);

    list.size -= 1;
  }

  bool is_empty_list() {
    return (this->head_link == nullptr || this->size == 0);
  }

  static void reset_list(my_linked_list& list) {
    if (!is_empty_list(list)) {
      link* curr_link = list.head_link;
      while (curr_link) {
        link* to_reset_link = curr_link;
        curr_link = curr_link->next_link;
        reset_link(*to_reset_link);
      }
    }
    list.head_link = nullptr;
    list.size = 0;
  }

  // TODO: loop -> for_each ?

  template <typename T>
  static void loop_list_links(my_linked_list& list, const std::function<void(T*)>& callback) {

    if (is_empty_list(list))
      return;

    link* curr_link = list.head_link;
    while (curr_link) {
      callback(static_cast<T*>(curr_link->user_data));
      curr_link = curr_link->next_link;
    }
  }

};






