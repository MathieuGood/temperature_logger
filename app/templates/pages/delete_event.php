<h3>Suppression d'un événement</h3>
<p>
    Êtes-vous certain de vouloir supprimer l'événement suivant ?
</p>
<p>
    <?php ?>
</p>
<?php
$id = $_GET['id'];

if (!isset($id)) {
    echo '<a href="index.php?page=gestion_evenements">Retour à la liste des événements</a>';
} else {
    ?>
    <form method="POST" action="">
        <input class="button redbutton" type="button" onclick="window.location.href = 'index.php?page=liste_users'" value="Annuler">
        <input class="button" type="submit" name="validation" value="Confirmer la suppression">
    </form>
    <?php
    if (isset($_POST['validation'])) {
        $events_db = new Events();
        $events_db->delete($id);
        header("Location: index.php?page=gestion_evenements");
    }
}

?>
