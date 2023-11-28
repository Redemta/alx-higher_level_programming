#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head of singly list
 * @number: integer to insert in list
 *
 * Return: new node on success, NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current->next != NULL && number > current->next->n)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;

	return (new);
}
