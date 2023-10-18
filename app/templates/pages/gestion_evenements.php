<h3>Gestion des événements</h3>
<?php
if (isset($_SESSION['open']) && $_SESSION['open'] > 0) {
    $events_db = new Events();
    $count_events = $events_db->countEvents();
    echo "Nombre d'événements dans la base : ".$count_events."<br />";
    ?>
    <input class="button" type="button" onclick="window.location.href = 'index.php?page=create_event'" value="Créer un nouvel événement">
    <br/><br/>

    <table class="table-with-borders">
        <tr>
            <th></th>
            <th>Date</th>
            <th>Heure</th>
            <th>Tarif</th>
            <th>Style</th>
            <th>Artiste</th>
            <!-- <th>Description</th> -->
        </tr>
        <tr>
        <?php

        $event_list = $events_db->getFullInfo();  

        foreach ($event_list as $event) {
            echo "<td><a href='index.php?page=delete_event&id=".$event['id_evenement']."'> ❌</a><a href='index.php?page=edit_event&id=".$event['id_evenement']."'> ✏ </a></td>";
            $date = strtotime($event['date_evenement']);
            echo "<td>".date("d/m/Y", $date)."</td>";
            $time = strtotime($event['heure_evenement']);
            echo "<td>".date("H:i", $time)."</td>";
            echo "<td>".$event['tarif_evenement']." €</td>";
            echo "<td>".$event['style_evenement']."</td>";
            echo "<td>".$event['artiste_evenement']."</td>";
            // echo "<td>".$event['texte_evenement']."</td>";
            echo "</tr>";
        }

    } else {
        header("Location: index.php?page=accueil");
    }
    ?>
    </table>