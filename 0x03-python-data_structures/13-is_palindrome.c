#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: points to head of node
 *
 * Return: 1 if palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *tmp;
	listint_t *first = prev;
	listint_t *second = (fast == NULL) ? slow : slow->next;

	if (*head == NULL && fast->next == NULL)
	{
		return (1);
	}
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}
	while (first != NULL && second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}
