#include <stdlib.h>
#include "lists.h"

/**
 * insert_node Inserts a new node into a sorted singly linked list
 * @head: Double pointer to the head of the list
 * @number: The number to insert
 *
 * Return: The address of the new node, or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new-node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
