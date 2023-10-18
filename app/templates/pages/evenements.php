<h3>Événements à venir</h3>

<?php
$events_db = new Events();
$event_list = $events_db->getFullInfoWithoutHistory();


foreach ($event_list as $event) {
?>
    <table>
        <tr>
            <td colspan="3" class="event-date"><?php $date = strtotime($event['date_evenement']); echo date("d/m/Y", $date); ?></td>
        </tr>
        <tr>
            <td colspan="3" class="artist-name"><?php echo $event['artiste_evenement'] ?></td>
        </tr>

        <tr>
            <th>Heure</th>
            <td><?php
                $time = strtotime($event['heure_evenement']);
                echo date("H:i", $time);
                // echo $event['heure_evenement']
                ?></td>
            <td rowspan="4" class="light-text"><?php echo $event['texte_evenement'] ?></td>
        </tr>

        <tr>
            <th>Tarif</th>
            <td><?php echo $event['tarif_evenement'] ?> €</td>
        </tr>

        <tr>
            <th>Style</th>
            <td><?php echo $event['style_evenement'] ?></td>
        </tr>
        <tr>
            <th></th>
            <td></td>
        </tr>
    </table>
    <br />

<?php
}
?>

