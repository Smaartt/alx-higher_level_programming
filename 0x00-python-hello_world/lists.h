
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s -sthe singly linked list
 * @n: the integer
 * @next: the points to the next node
 *
 * Description: the singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);

#endif /* LISTS_H */

