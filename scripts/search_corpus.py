"""Query a local FTS5 reference DB. Results locate context, not verified facts."""
import argparse,pathlib,sqlite3
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('database',type=pathlib.Path);ap.add_argument('query');ap.add_argument('--limit',type=int,default=10)
args=ap.parse_args()
db=sqlite3.connect(args.database.resolve().as_uri()+'?mode=ro',uri=True)
try:
    rows=db.execute('SELECT episode_id,date,timestamp,speaker,snippet(transcript,4,"[", "]"," … ",40),path FROM transcript WHERE transcript MATCH ? ORDER BY rank LIMIT ?',(args.query,max(1,min(args.limit,100)))).fetchall()
except sqlite3.OperationalError as exc:raise SystemExit(f'Invalid FTS query or database: {exc}')
finally:db.close()
for eid,date,timestamp,speaker,snippet,path in rows:
    print(f'{date} | {eid} | {timestamp} | {speaker}\n{snippet}\nSource: {path}\n')
